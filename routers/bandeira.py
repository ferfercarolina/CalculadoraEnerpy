from fastapi import APIRouter
from models.bandeira import BandeiraDB
from schemas.bandeira import BandeiraCreate, BandeiraRead, BandeiraReadList, BandeiraUpdate

router = APIRouter(prefix='/bandeiras', tags=['BANDEIRAS'])

@router.post('', response_model=BandeiraRead)
def criar_bandeira(nova_bandeira: BandeiraCreate):
    bandeira = BandeiraDB.create(**nova_bandeira.model_dump())
    return bandeira

@router.get('', response_model=BandeiraReadList)
def listar_bandeiras():
    bandeiras = BandeiraDB.select()
    return {'bandeiras': bandeiras}

@router.get('/{bandeira_id}', response_model=BandeiraRead)
def listar_bandeira(bandeira_id: int):
    bandeira = BandeiraDB.get_or_none(BandeiraDB.id == bandeira_id)
    return bandeira

@router.patch('/{bandeira_id}', response_model=BandeiraRead)
def atualizar_bandeira(bandeira_id: int, bandeira_atualizada: BandeiraUpdate):
    bandeira = BandeiraDB.get_or_none(BandeiraDB.id == bandeira_id)
    if bandeira:
        bandeira.nome = bandeira_atualizada.nome
        bandeira.tarifa = bandeira_atualizada.tarifa
        bandeira.save()
    return bandeira

@router.delete('/{bandeira_id}', response_model=BandeiraRead)
def excluir_bandeira(bandeira_id: int):
    bandeira = BandeiraDB.get_or_none(BandeiraDB.id == bandeira_id)
    if bandeira:
        bandeira.delete_instance()
    return bandeira
