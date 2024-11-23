int potenciometro = A0; //pin analogico del potenciometro
int led = 9; //pin donde esta conectado led
int valor; //valor del potenciometro
int brillo; //valor para almacenar el brillo

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(led,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  valor = analogRead(potenciometro); //obtiene el valor del potenciometro
  brillo = map(valor, 0, 1023, 0, 255); //mapea el valor obtenido a un rango entre 0 y 255
  // map(valor, rango potenciometro menor, " mayor, rango led menor, " mayor)
  analogWrite(led,brillo); //aplica al led el valor obtenido del brillo
  Serial.println(valor);

  delay(1000);
}
