from typing import Optional
from pydantic import BaseModel, Field


class RawExtractedItems(BaseModel):
    """Raw line item extracted from an Excel sheet row before semantic processing."""

    label: str = Field(
        ..., 
        description="The textual line item description from Excel"
    )
    value: float = Field(
        ...,
        description="Numeric magnitude (negative ONLY if parenthetical or explicit minus)",
    )
    source_file: str = Field(
        ..., 
        description="Name of the source Excel file"
    )
    source_sheet: str = Field(
        ..., 
        description="Name of the source worksheet"
    )
    row_index: int = Field(
        ..., 
        ge=1, 
        description="1-based row index in Excel"
    )
    column_label: Optional[str] = Field(
        default=None, 
        description="Column identifier for the label (e.g., 'Col_1')"
    )
    value_column: Optional[str] = Field(
        default=None, 
        description="Column identifier for the value (e.g., 'Col_2')"
    )
    balance_type: Optional[str] = Field(
        default=None, 
        description="Captured 'Dr', 'Cr', or None if unspecified"
    )
    currency: Optional[str] = Field(
        default=None, 
        description="Captured currency symbol or ISO code (e.g., '$', 'EUR', 'AED')"
    )
    period: Optional[str] = Field(
        default=None, 
        description="Captured time period header (e.g., 'FY 2024', 'Q3 2025')"
    )


class ExtractedData(BaseModel):
    """Line item undergoing semantic classification and mapping."""

    label: str = Field(
        ..., 
        description="Textual description from the Excel row"
    )
    raw_value: str = Field(
        ..., 
        description="Original raw cell string as displayed before parsing"
    )
    internal_name: Optional[str] = Field(
        default=None,
        description="Standardized chart-of-accounts account name (e.g., 'Total_Revenue')",
    )
    cleaned_value: Optional[float] = Field(
        default=None, 
        description="Parsed numeric float value"
    )
    status: str = Field(
        default="raw",
        description="Processing state (e.g., 'raw', 'mapped', 'error')",
    )


class FinalExtractedResults(BaseModel):
    """Overall extraction payload including row items and document viability metrics."""

    rows: list[ExtractedData] = Field(
        ..., 
        description="List of extracted data rows"
    )
    missing_required: list[str] = Field(
        default_factory=list,
        description="List of required financial accounts that could not be mapped",
    )
    is_viable: bool = Field(
        ...,
        description="True if statement contains enough valid required fields to process",
    )