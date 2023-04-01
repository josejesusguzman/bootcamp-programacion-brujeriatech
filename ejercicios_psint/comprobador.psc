// Comprobador de mayoria de edad
// Comprobar que una persona sea mayor de 18 años
// Comprobar que la persona no tenga más de 130 años
// Comprobar que la persona exista, es decir, que tenga más de 0 años

Proceso comprobador
	Escribir "Ingresa tu edad"
	Leer edad
	Si edad >= 18 Y edad <= 130
		Entonces
			Escribir "Pasale al mamitas"
		SiNo
			Si edad < 0 O edad > 130 
				Entonces 
					Escribir "No deberías existir"
				Sino
					Si edad < 18 Entonces
						Escribir "Tas muuuuy chikitho"
					FinSi
			FinSi
			
	FinSi
FinProceso
