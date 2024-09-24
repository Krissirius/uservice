"""Add foreign key to users table

Revision ID: 70bda8b7dcb3
Revises: d4fba6b28281
Create Date: 2024-09-24 13:22:25.783591

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '70bda8b7dcb3'
down_revision: Union[str, None] = 'd4fba6b28281'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Добавляем внешний ключ
    op.add_column('users', sa.Column('idDepartment', sa.Integer(), nullable=True))
    op.create_foreign_key(
        'fk_users_idDepartment',  # имя ограничения
        'users',  # имя таблицы, где добавляем внешний ключ
        'ref_departments',  # имя таблицы, на которую ссылаемся
        ['idDepartment'],  # столбец в таблице users
        ['id']  # столбец в таблице ref_departments
    )

def downgrade() -> None:
    # Удаляем внешний ключ
    op.drop_constraint('fk_users_idDepartment', 'users', type_='foreignkey')
    op.drop_column('users', 'idDepartment')