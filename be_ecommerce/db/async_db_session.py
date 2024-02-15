"""This module defines the database connection and how it works."""

import asyncio
import contextlib
from typing import AsyncIterator

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class AsyncDatabaseSession:
    """Asynchronous database session."""

    def __init__(self) -> None:
        self.database_url = settings.database_url
        self.engine = create_async_engine(
            self.database_url,
            isolation_level="AUTOCOMMIT",
            echo=settings.db_echo,
            future=True,
            echo_pool=False,
            pool_size=settings.db_pool_size,
            max_overflow=settings.db_max_overflow,
            pool_pre_ping=True,
        )
        self.async_session = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            future=True,
            expire_on_commit=False,
            autocommit=False,
        )

    async def init_db(self):
        """Initialize database."""
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    @contextlib.asynccontextmanager
    async def get_session(self) -> AsyncIterator[AsyncSession]:
        """Getter for database session."""
        session = self.async_session()
        try:
            yield session
        except SQLAlchemyError:
            # logger.exception("Catched SQLAlchemyError")
            raise
        finally:
            await asyncio.shield(session.close())
