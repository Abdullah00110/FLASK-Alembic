"""User

Revision ID: fecd6dd9811b
Revises: 
Create Date: 2023-12-29 11:40:18.567934

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fecd6dd9811b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "user",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("username", sa.String(50), unique=True, nullable=False),
        sa.Column("email", sa.String(120), unique=True, nullable=False)


    )


def downgrade() -> None:
    op.drop_table("user")
