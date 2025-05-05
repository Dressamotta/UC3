import json

# Dicionário para armazenar tarefas
tarefas = {
    1: {"titulo": "Estudar Python", "status": "pendente"},
    2: {"titulo": "Fazer relatório", "status": "concluído"}
}

# Conjunto de status válidos
status_validos = {"pendente", "em andamento", "concluído"}

def listar_tarefas():
    """Retorna todas as tarefas em formato JSON."""
    return json.dumps(tarefas, indent=4, ensure_ascii=False)

def adicionar_tarefa(id, titulo, status):
    """Adiciona uma nova tarefa, validando o ID e o status."""
    if id in tarefas:
        return "Erro: ID já existe."
    if status not in status_validos:
        return "Erro: Status inválido."
    
    tarefas[id] = {"titulo": titulo, "status": status}
    return "Tarefa adicionada com sucesso."

def atualizar_status(id, novo_status):
    """Atualiza o status de uma tarefa existente."""
    if id not in tarefas:
        return "Erro: ID não encontrado."
    if novo_status not in status_validos:
        return "Erro: Status inválido."
    
    tarefas[id]["status"] = novo_status
    return "Status atualizado com sucesso."

def remover_tarefa(id):
    """Remove uma tarefa pelo ID."""
    if id not in tarefas:
        return "Erro: ID não encontrado."
    
    del tarefas[id]
    return "Tarefa removida com sucesso."

# Testes
print(listar_tarefas())
print(adicionar_tarefa(3, "Comprar suprimentos", "pendente"))
print(atualizar_status(1, "em andamento"))
print(remover_tarefa(2))
print(listar_tarefas())
