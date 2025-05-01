import os
import sys

from litestar import Litestar
from litestar.plugins.sqlalchemy import (
    AsyncSessionConfig,
    SQLAlchemyAsyncConfig,
    SQLAlchemyPlugin,
)
from dotenv import load_dotenv

from controllers import UserController

load_dotenv()

DB_USER = os.getenv('DB_USER', '')
DB_PASSWORD = os.getenv('DB_PASSWORD', '')
DB_HOST = os.getenv('DB_HOST', '')
DB_PORT = os.getenv('DB_PORT', '')
DB_NAME = os.getenv('DB_NAME', '')


if not DB_HOST or not DB_PORT or not DB_NAME:
    print('DB_HOST / DB_PORT / DB_NAME required environment param')
    sys.exit(100)


# session_config = AsyncSessionConfig(expire_on_commit=False)
sqlalchemy_config = SQLAlchemyAsyncConfig(
    # connection_string="sqlite+aiosqlite:///test.sqlite",
    connection_string=f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
    before_send_handler="autocommit",
    session_config=AsyncSessionConfig(expire_on_commit=False),
    create_all=True,
)
alchemy = SQLAlchemyPlugin(config=sqlalchemy_config)

app = Litestar(route_handlers=[UserController],
               plugins=[alchemy],
               debug=True)
