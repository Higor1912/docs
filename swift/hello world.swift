import Foundation

print("Turno")
if let turno = readLine(), !turno.isEmpty {
    print("Salario")
    if let salarioInput = readLine(), let salarioValue = Double(salarioInput) {
        let inss = (salarioValue / 100) * 11
        let fgts = (salarioValue / 100) * 8
        let recebe = salarioValue - fgts - inss

        print("Receber \(recebe)")

        if recebe >= 1201 {
            print("Receber em TED")
        } else {
            print("Receber em PIX")
        }
    } else {
        print("Salário inválido")
    }
} else {
    print("Turno inválido")
}