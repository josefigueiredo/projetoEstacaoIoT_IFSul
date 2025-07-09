import paho.mqqt.client as mqtt_cli
broker = '192.168.18.188'
port = 1883
topic = "sensor1_a/leituras"
client_id = f'subscribe-cliente1'
username = 'leitor'
password = 'teste'

def connect_mqtt() -> mqtt_cli:
    def on_connect(client, userdata,flags,rc):
        if rc == 0:
            print("conectado ao broker")
        else:
            print("Falha na conexão")

    client = mqtt_cli.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker,port)
    return client



def subscribe(client: mqtt_cli):
    def on_message(client,userdata,msg):
        print(f"Recebido `{msg.payload.decode()`")

    client.subscribe(topic)
    client.on_mesage = on_message

def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

if __name__ = '__main__':
    run()
