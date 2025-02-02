"""Index the columns used by the listing and reporting queries.

Revision ID: 0003_indexes
Revises: 0002_users
Create Date: 2025-05-18 16:05:00
"""

from alembic import op

revision = "0003_indexes"
down_revision = "0002_users"
branch_labels = None
depends_on = None


def upgrade():
    op.create_index("ix_entries_user_start", "entries", ["user_id", "start"])
    op.create_index("ix_entries_user_end", "entries", ["user_id", "end"])
    op.create_index("ix_projects_user_archived", "projects", ["user_id", "archived"])


def downgrade():
    op.drop_index("ix_projects_user_archived", table_name="projects")
    op.drop_index("ix_entries_user_end", table_name="entries")
    op.drop_index("ix_entries_user_start", table_name="entries")
