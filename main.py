import network, time, urequests
from machine import Pin, ADC, PWM
from utelegram import Bot
from servo import Servo

TOKEN = '(Tu token de bot de telegram)'

bot = Bot(TOKEN)
sg90_servo = Servo(pin=(13))




def conectaWifi (red, password):
      global miRed
      miRed = network.WLAN(network.STA_IF)     
      if not miRed.isconnected():              #Si no está conectado…
          miRed.active(True)                   #activa la interface
          miRed.connect(red, password)         #Intenta conectar con la red
          print('Conectando a la red', red +"…")
          timeout = time.time ()
          while not miRed.isconnected():           #Mientras no se conecte..
              if (time.ticks_diff (time.time (), timeout) > 10):
                  return False
      return True

if conectaWifi ("(Nombre Red wifi)", "(Contraseña de la red wifi)"):  #Red wifi a la que se conectara el ESP32

    print ("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())

    @bot.add_message_handler('Inicio')
    def help(update):
      update.reply('''Menu principal
                            
                     Dar comida''')

    @bot.add_message_handler('Dar comida')
    def comida(update):
      sg90_servo.move(0)  # Mueve el servomotor 0°.
      time.sleep(1)
      sg90_servo.move(90)  # Mueve el servomotor 90°.
      time.sleep(3)
      update.reply('gracias por alimentarme')

    bot.start_loop()

else:
       print ("Imposible conectar")
       miRed.active (False)