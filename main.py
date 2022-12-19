import AccesoDatosTrabajador as ac
import ConfigurationManager as conf
import Personalizacion as p

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # a = ac.grabaTrabajador(True, -1, "Loli", "Vazquez Piñeiro", "7pj10hnoyt@earthling.net", "Mujer")

    b = ac.listaTrabajadorNo()

    for i in b:
        print(i.getNombre()+", sexo:"+i.getSexo())

