using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace turnosdetrabajadores
{
    class turnosdetrabajadores
    {
        private float[] turnoMan;
        private float[] turnoTar;

        public void Cargar() 
        {
            string linea;
            turnoMan=new float[4];
            turnoTar=new float[4];
            Console.WriteLine("----- Los Sueldos de los Empleados de la Mañana -----");
            for(int a = 0; a < 4; a++) 
            {
                Console.Write("Ingrese su sueldo:");
                linea = Console.ReadLine();              
                turnoMan[a]=float.Parse(linea);
            }
            Console.WriteLine("----- Los Sueldos de los Empleados de la Tarde -----");
            for(int a = 0; a < 4; a++) 
            {
                Console.Write("Ingrese su sueldo:");
                linea = Console.ReadLine();              
                turnoTar[a]=float.Parse(linea);
            }
        }

        public void CalcularGastos() 
        {
            float man=0;
            float tar=0;
            for(int a = 0; a < 4; a++)
            {
                man=man+turnoMan[a];
                tar=tar+turnoTar[a];
            }
            Console.WriteLine("Total del monto del turno de la mañana:"+man);
            Console.WriteLine("Total del monto del turno de la tarde:"+tar);
            Console.ReadKey();
        }

        static void Main(string[] args)
        {
            turnosdetrabajadores p = new turnosdetrabajadores();
            p.Cargar();
            p.CalcularGastos();
        }
    }
}