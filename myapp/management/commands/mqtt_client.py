import paho.mqtt.client as mqtt
from django.core.management.base import BaseCommand
from myapp.models import DataDump

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        client = mqtt.Client()

        def on_connect(client, userdata, flags, rc):
            self.stdout.write('Connected with result code ' + str(rc))
            client.subscribe('test/topic')

        def on_message(client, userdata, msg):
            self.stdout.write(f'Message received: {msg.payload.decode()}')
            # Process and save the message to database
            data = msg.payload.decode()
            y = data.split(', ')
            DataDump.objects.create(field1=y[0], field2=int(y[1]), field3=y[2])

        client.on_connect = on_connect
        client.on_message = on_message

        client.connect('127.0.0.1', 1883, 60)
        client.loop_forever()



