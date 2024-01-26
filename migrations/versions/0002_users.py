"""Add users and per-user scoping.

Revision ID: 0002_users
Revises: 0001_initial
Create Date: 2024-02-11 09:40:00
"""

from alembic import op
import sqlalchemy as sa

revision = "0002_users"
down_revision = "0001_initial"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("display_name", sa.String(length=120), nullable=False, server_default=""),
        sa.Column("password_hash", sa.String(length=255), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column("created_at", sa.DateTime(), nullable=False),
    )
    op.create_index("ix_users_email", "users", ["email"], unique=True)

    with op.batch_alter_table("projects") as batch:
        batch.add_column(sa.Column("user_id", sa.Integer(), nullable=True))
        batch.create_foreign_key("fk_projects_user", "users", ["user_id"], ["id"])
        batch.drop_constraint("projects_name_key", type_="unique")
        batch.create_unique_constraint("uq_projects_user_name", ["user_id", "name"])

    with op.batch_alter_table("entries") as batch:
        batch.add_column(sa.Column("user_id", sa.Integer(), nullable=True))
        batch.create_foreign_key("fk_entries_user", "users", ["user_id"], ["id"])
        batch.create_index("ix_entries_user_id", ["user_id"])


def downgrade():
    with op.batch_alter_table("entries") as batch:
        batch.drop_index("ix_entries_user_id")
        batch.drop_constraint("fk_entries_user", type_="foreignkey")
        batch.drop_column("user_id")

    with op.batch_alter_table("projects") as batch:
        batch.drop_constraint("uq_projects_user_name", type_="unique")
        batch.drop_constraint("fk_projects_user", type_="foreignkey")
        batch.drop_column("user_id")

    op.drop_index("ix_users_email", table_name="users")
    op.drop_table("users")
