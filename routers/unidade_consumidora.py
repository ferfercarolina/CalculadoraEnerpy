from fastapi import APIRouter
from models.unidade_consumidora import UnidadeConsumidoraDB
from schemas.unidade_consumidora import UnidadeConsumidoraCreate, UnidadeConsumidoraRead, UnidadeConsumidoraReadList, UnidadeConsumidoraUpdate

router = APIRouter(prefix='/unidades-consumidoras', tags=['UNIDADES CONSUMIDORAS'])

@router.post('', response_model=UnidadeConsumidoraRead)
def criar_unidade_consumidora(nova_unidade_consumidora: UnidadeConsumidoraCreate):
    unidade_consumidora = UnidadeConsumidoraDB.create(**nova_unidade_consumidora.model_dump())
    return unidade_consumidora

@router.get('', response_model=UnidadeConsumidoraReadList)
def listar_unidades_consumidoras():
    unidades_consumidoras = UnidadeConsumidoraDB.select()
    return {'unidades_consumidoras': unidades_consumidoras}

@router.get('/{id_consumidor}', response_model=UnidadeConsumidoraRead)
def listar_unidade_consumidora(id_consumidor: int):
    unidade_consumidora = UnidadeConsumidoraDB.get_or_none(UnidadeConsumidoraDB.id == id_consumidor)
    return unidade_consumidora

@router.patch('/{id_consumidor}', response_model=UnidadeConsumidoraRead)
def atualizar_unidade_consumidora(id_consumidor: int, consumidor_atualizada: UnidadeConsumidoraUpdate):
    unidade_consumidora = UnidadeConsumidoraDB.get_or_none(UnidadeConsumidoraDB.id == id_consumidor)
    if unidade_consumidora:
        unidade_consumidora.nome = consumidor_atualizada.nome
        unidade_consumidora.save()
    return unidade_consumidora

@router.delete('/{id_consumidor}', response_model=UnidadeConsumidoraRead)
def excluir_unidade_consumidora(id_consumidor: int):
    unidade_consumidora = UnidadeConsumidoraDB.get_or_none(UnidadeConsumidoraDB.id == id_consumidor)
    if unidade_consumidora:
        unidade_consumidora.delete_instance()
    return unidade_consumidora
