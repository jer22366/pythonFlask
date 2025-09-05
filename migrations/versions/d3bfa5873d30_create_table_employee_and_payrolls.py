"""create_table_employee_and_payRolls

Revision ID: d3bfa5873d30
Revises: 1f2c1678c562
Create Date: 2025-09-05 11:48:55.143148

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd3bfa5873d30'
down_revision = '1f2c1678c562'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'employees',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('employee_code', sa.String(20), nullable=False, unique=True),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('department', sa.String(50)),
        sa.Column('position', sa.String(50)),
        sa.Column('hire_date', sa.Date, nullable=False)
    )

    op.create_table(
        'payrolls',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('employee_id', sa.Integer, sa.ForeignKey('employees.id'), nullable=False),
        sa.Column('month', sa.Date, nullable=False),
        sa.Column('base_salary', sa.Float, nullable=False, default=0.0),
        sa.Column('total_allowance', sa.Float, nullable=False, default=0.0),
        sa.Column('total_bonus', sa.Float, nullable=False, default=0.0),
        sa.Column('total_deduction', sa.Float, nullable=False, default=0.0),
        sa.Column('net_salary', sa.Float, nullable=False, default=0.0),
        sa.Column('created_at', sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, server_default=sa.func.now(), onupdate=sa.func.now())
    )

    op.create_table(
        'allowances',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('payroll_id', sa.Integer, sa.ForeignKey('payrolls.id'), nullable=False),
        sa.Column('type', sa.String(50), nullable=False),
        sa.Column('amount', sa.Float, nullable=False, default=0.0)
    )

    op.create_table(
        'bonuses',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('payroll_id', sa.Integer, sa.ForeignKey('payrolls.id'), nullable=False),
        sa.Column('type', sa.String(50), nullable=False),
        sa.Column('amount', sa.Float, nullable=False, default=0.0)
    )

    op.create_table(
        'deductions',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('payroll_id', sa.Integer, sa.ForeignKey('payrolls.id'), nullable=False),
        sa.Column('type', sa.String(50), nullable=False),
        sa.Column('amount', sa.Float, nullable=False, default=0.0)
    )


def downgrade():
    op.drop_table('deductions')
    op.drop_table('bonuses')
    op.drop_table('allowances')
    op.drop_table('payrolls')
    op.drop_table('employees')

    # ### end Alembic commands ###
