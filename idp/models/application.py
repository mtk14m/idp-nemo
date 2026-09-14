from datetime import datetime
from enum import Enum
from sqlalchemy import Enum as SQLEnum, func
from sqlalchemy.orm import Mapped, mapped_column
from core.database import Base

class EnvironmentType(str, Enum):
    DEV = "dev"
    STAGING = "staging"
    PROD = "prod"

class StatusType(str, Enum):
    PROVISIONING = "provisioning"
    RUNNING = "running"
    FAILED = "failed"

class Application(Base):
    __tablename__ = "applications"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    environment: Mapped[EnvironmentType] = mapped_column(SQLEnum(EnvironmentType))
    status: Mapped[StatusType] = mapped_column(SQLEnum(StatusType))
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
  