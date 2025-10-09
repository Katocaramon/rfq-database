from sqlalchemy import (
    Column, Integer, String, Text, Date, Float, ForeignKey, UniqueConstraint,
    CheckConstraint, Computed
)
from sqlalchemy.orm import relationship, Mapped, mapped_column
from db import Base


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)


class RFQ(Base):
    __tablename__ = "rfq"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome_cliente: Mapped[str] = mapped_column(String(120), nullable=False)
    nome_progetto: Mapped[str] = mapped_column(String(120), nullable=False)
    data_ricezione: Mapped[Date] = mapped_column(Date, nullable=False)
    due_date_quotazione: Mapped[Date] = mapped_column(Date, nullable=False)
    target_price: Mapped[float | None] = mapped_column(Float, nullable=True)
    descrizione: Mapped[str | None] = mapped_column(Text, nullable=True)

    # ✅ Nuovo campo "stato" per tracciare la fase della RFQ
    stato: Mapped[str] = mapped_column(
        String(15),
        nullable=False,
        default="attiva"
    )

    __table_args__ = (
        UniqueConstraint("nome_cliente", "nome_progetto", name="uq_cliente_progetto"),
        CheckConstraint("stato in ('attiva', 'inattiva', 'vinta', 'persa')", name="ck_rfq_stato"),
    )

    offerte = relationship("Offerta", back_populates="rfq", cascade="all, delete-orphan")
    documents = relationship("Document", back_populates="rfq", cascade="all, delete-orphan")


class Offerta(Base):
    __tablename__ = "offerte"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rfq_id: Mapped[int] = mapped_column(ForeignKey("rfq.id", ondelete="CASCADE"), nullable=False)
    codice_pm: Mapped[str] = mapped_column(String(80), nullable=False)
    id_offerta_rev: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    versione: Mapped[str | None] = mapped_column(String(30), nullable=True)
    stato: Mapped[str] = mapped_column(String(10), nullable=False, default="attiva")
    data_offerta: Mapped[Date] = mapped_column(Date, nullable=False)

    # Prezzi
    prezzo_sop: Mapped[float | None] = mapped_column(Float, nullable=True)
    prezzo_sop1: Mapped[float | None] = mapped_column(Float, nullable=True)
    prezzo_sop2: Mapped[float | None] = mapped_column(Float, nullable=True)
    prezzo_sop3: Mapped[float | None] = mapped_column(Float, nullable=True)
    prezzo_sop4: Mapped[float | None] = mapped_column(Float, nullable=True)

    # GM (%)
    gm_sop: Mapped[float | None] = mapped_column(Float, nullable=True)
    gm_sop1: Mapped[float | None] = mapped_column(Float, nullable=True)
    gm_sop2: Mapped[float | None] = mapped_column(Float, nullable=True)
    gm_sop3: Mapped[float | None] = mapped_column(Float, nullable=True)
    gm_sop4: Mapped[float | None] = mapped_column(Float, nullable=True)

    # Volumi
    vol_sop: Mapped[int | None] = mapped_column(Integer, nullable=True)
    vol_sop1: Mapped[int | None] = mapped_column(Integer, nullable=True)
    vol_sop2: Mapped[int | None] = mapped_column(Integer, nullable=True)
    vol_sop3: Mapped[int | None] = mapped_column(Integer, nullable=True)
    vol_sop4: Mapped[int | None] = mapped_column(Integer, nullable=True)

    # Fatturati (colonne generate)
    fatt_sop = Column(Float, Computed("(IFNULL(prezzo_sop,0.0)*IFNULL(vol_sop,0))"))
    fatt_sop1 = Column(Float, Computed("(IFNULL(prezzo_sop1,0.0)*IFNULL(vol_sop1,0))"))
    fatt_sop2 = Column(Float, Computed("(IFNULL(prezzo_sop2,0.0)*IFNULL(vol_sop2,0))"))
    fatt_sop3 = Column(Float, Computed("(IFNULL(prezzo_sop3,0.0)*IFNULL(vol_sop3,0))"))
    fatt_sop4 = Column(Float, Computed("(IFNULL(prezzo_sop4,0.0)*IFNULL(vol_sop4,0))"))

    __table_args__ = (
        UniqueConstraint("rfq_id", "id_offerta_rev", name="uq_offerta_rfq_rev"),
        CheckConstraint("stato in ('attiva','passata')", name="ck_stato"),
    )

    rfq = relationship("RFQ", back_populates="offerte")
    documents = relationship("Document", back_populates="offerta", cascade="all, delete-orphan")


class Document(Base):
    __tablename__ = "documents"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rfq_id: Mapped[int | None] = mapped_column(ForeignKey("rfq.id", ondelete="CASCADE"), nullable=True)
    offerta_id: Mapped[int | None] = mapped_column(ForeignKey("offerte.id", ondelete="CASCADE"), nullable=True)
    filename: Mapped[str] = mapped_column(String(255), nullable=False)
    path: Mapped[str] = mapped_column(String(255), nullable=False)

    rfq = relationship("RFQ", back_populates="documents")
    offerta = relationship("Offerta", back_populates="documents")