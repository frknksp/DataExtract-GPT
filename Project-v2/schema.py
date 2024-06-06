from typing import Optional
from langchain_core.pydantic_v1 import BaseModel, Field, Json

# Bu sınıf, karaciğerle ilgili tıbbi raporların yapılandırılmış temsilidir.
# Sınıfa yeni alanlar ekleyerek çıkarılması istenen özellikler değiştirilebilir.
class KaracigerRaporu(BaseModel):
    """Structured representation of liver-related medical reports."""

    karaciger_uzunluk_cm: Optional[float] = Field(
        default=None, description="The cranio-caudal dimension of the liver in centimeters"
    )
    karaciger_yogunluk: Optional[str] = Field(
        default=None, description="Density of liver parenchyma indicating any abnormalities"
    )
    safrakesesi: Optional[str] = Field(
        default=None, description="Description of gallbladder condition"
    )
    dalak_uzunluk_cm: Optional[float] = Field(
        default=None, description="The size of the spleen in centimeters"
    )
    pankreas: Optional[str] = Field(
        default=None, description="Description of pancreas condition"
    )
    adrenal_bezler: Optional[str] = Field(
        default=None, description="Description of adrenal glands condition"
    )
    bobrekler: Optional[str] = Field(
        default=None, description="Description of kidneys condition"
    )
    ureter: Optional[str] = Field(
        default=None, description="Description of ureters condition"
    )
    duodenum: Optional[str] = Field(
        default=None, description="Description of duodenum condition"
    )
    mesane: Optional[str] = Field(
        default=None, description="Description of bladder condition"
    )
    over: Optional[str] = Field(
        default=None, description="Description of ovaries condition"
    )
    lenf_bezi: Optional[str] = Field(
        default=None, description="Description of any pathological lymph nodes"
    )
    batin_ici_serbest_sivi: Optional[str] = Field(
        default=None, description="Description of any free fluid in the abdomen"
    )
    kemik_yapilari: Optional[str] = Field(
        default=None, description="Description of any abnormalities in bone structures"
    )
    pulmonary_nodules: Optional[str] = Field(
        default=None, description="Description of pulmonary nodules"
    )
    kolon: Optional[str] = Field(
        default=None, description="Description of colon condition"
    )
    uterus: Optional[str] = Field(
        default=None, description="Description of uterus condition"
    )