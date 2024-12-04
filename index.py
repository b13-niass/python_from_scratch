from classes.Client import Client

client = Client("Bob", "bob@example.com",20000, 12345)

client.teste_order() # Celui de User est appelé, puis qu'il est le premier à être hérité