from fastapi import APIRouter
from models.tipo_dispositivo import TipoDispositivoDB
from schemas.tipo_dispositivo import TipoDispositivoCreate, TipoDispositivoRead, TipoDispositivoReadList, TipoDispositivoUpdate

router = APIRouter(prefix='/tipos-dispositivos', tags=['TIPOS DE DISPOSITIVOS'])

@router.post('', response_model=TipoDispositivoRead)
def criar_tipo_de_dispositivo(novo_tipo: TipoDispositivoCreate):
    tipo = TipoDispositivoDB.create(**novo_tipo.model_dump())
    return tipo

@router.get('', response_model=TipoDispositivoReadList)
def listar_tipos_de_dispositivos():
    tipos = TipoDispositivoDB.select()
    return {'tipos_dispositivos': tipos}

@router.get('/{tipo_dispositivo_id}', response_model=TipoDispositivoRead)
def listar_tipo_de_dispositivo(tipo_dispositivo_id: int):
    tipo = TipoDispositivoDB.get_or_none(TipoDispositivoDB.id == tipo_dispositivo_id)
    return tipo

@router.patch('/{tipo_dispositivo_id}', response_model=TipoDispositivoRead)
def atualizar_tipo_de_dispositivo(tipo_dispositivo_id: int, tipo_atualizado: TipoDispositivoUpdate):
    tipo = TipoDispositivoDB.get_or_none(TipoDispositivoDB.id == tipo_dispositivo_id)
    if tipo:
        tipo.nome = tipo_atualizado.nome
        tipo.save()
    return tipo

@router.delete('/{tipo_dispositivo_id}', response_model=TipoDispositivoRead)
def excluir_tipo_de_dispositivo(tipo_dispositivo_id: int):
    tipo = TipoDispositivoDB.get_or_none(TipoDispositivoDB.id == tipo_dispositivo_id)
    if tipo:
        tipo.delete_instance()
    return tipo
