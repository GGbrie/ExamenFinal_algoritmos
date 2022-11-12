using System;

namespace alturas_personas
{
    class alturas_personas
    {
        private float[] altura;
        private float promedio;

        public void Cargar() 
        {
            altura=new float[5];
            for (int a = 0; a < 5; a++)
            {
                Console.Write("Ingrese la altura de la persona:");
                string linea = Console.ReadLine();
                altura[a] = float.Parse(linea);
            }
        }
    
        public void CalcularPromedio() 
        {
            float suma;
            suma=0;
            for(int a=0; a < 5; a++) 
            {
                suma=suma+altura[a];
            }
            promedio=suma/5;
            Console.WriteLine("Promedio total en alturas:"+promedio);
        }

        public void MayoresMenores() 
        {
            int may,men;
            may=0;
            men=0;
            for(int a = 0; a < 5; a++) 
            {
                if (altura[a] > promedio) 
                {
	                may++;
                }
                else
                {
                    if (altura[a] < promedio) 
                    {
                        men++;
                    }
                }
            }
            Console.WriteLine("Personas mayores al promedio:"+may);
            Console.WriteLine("Personas menores al promedio:"+men);
            Console.ReadKey();
        }
        static void Main(string[] args)
        {
            alturas_personas ap = new alturas_personas();
            ap.Cargar();
            ap.CalcularPromedio();
            ap.MayoresMenores();
        }
    }
}