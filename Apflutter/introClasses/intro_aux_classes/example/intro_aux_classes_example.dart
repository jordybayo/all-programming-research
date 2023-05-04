
class Microphone{
  // instances variables, propriete de l'instance
  String name;
  String color;
  int model = 4836;
}

void main() {

  var mic = Microphone();

  mic.name = "condenseur studio"; // .(dot) permet d'acceder au proprietes
  mic.color = "or";
  mic.model = 4578;

  print(mic.name);
}

