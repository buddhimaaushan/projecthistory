"""Create entries, projects and tags.

Revision ID: 0001_initial
Revises:
Create Date: 2022-03-06 11:20:00
"""

from alembic import op
import sqlalchemy as sa

revision = "0001_initial"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "projects",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(length=120), nullable=False, unique=True),
        sa.Column("colour", sa.String(length=7), nullable=False),
        sa.Column("archived", sa.Boolean(), nullable=False, server_default=sa.false()),
    )
    op.create_table(
        "tags",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(length=60), nullable=False, unique=True),
    )
    op.create_table(
        "entries",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("label", sa.String(length=200), nullable=False),
        sa.Column("start", sa.DateTime(), nullable=False),
        sa.Column("end", sa.DateTime(), nullable=True),
        sa.Column("project_id", sa.Integer(), sa.ForeignKey("projects.id"), nullable=True),
    )
    op.create_index("ix_entries_start", "entries", ["start"])
    op.create_table(
        "entry_tags",
        sa.Column("entry_id", sa.Integer(), sa.ForeignKey("entries.id", ondelete="CASCADE"), primary_key=True),
        sa.Column("tag_id", sa.Integer(), sa.ForeignKey("tags.id", ondelete="CASCADE"), primary_key=True),
    )


def downgrade():
    op.drop_table("entry_tags")
    op.drop_index("ix_entries_start", table_name="entries")
    op.drop_table("entries")
    op.drop_table("tags")
    op.drop_table("projects")
