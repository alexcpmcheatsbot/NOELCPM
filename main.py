#!/usr/bin/python

from noelcpm import CPMnoelcpm
from pystyle import Colorate, Colors
from rich.console import Console
import time

console = Console()
cpm = CPMnoelcpm()

def main():
    print(Colorate.Horizontal(Colors.red_to_white, """
███╗   ██╗██╗   ██╗      ███████╗████████╗ ██████╗ ██████╗ ███████╗
████╗  ██║██║   ██║      ██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗██╔════╝
██╔██╗ ██║██║   ██║█████╗███████╗   ██║   ██║   ██║██████╔╝███████╗
██║╚██╗██║██║   ██║╚════╝╚════██║   ██║   ██║   ██║██╔══██╗╚════██║
██║ ╚████║╚██████╔╝      ███████║   ██║   ╚██████╔╝██║  ██║███████║
╚═╝  ╚═══╝ ╚═════╝       ╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝
                         🏪 NV STORE
"""))

    console.print("🎮 [bold red]Painel NV STORE — Serviços Ativos[/bold red]\n")

    email = console.input("[bold cyan]📧 E-mail da conta: [/bold cyan]")
    senha = console.input("[bold cyan]🔐 Senha da conta: [/bold cyan]")

    if not cpm.login(email, senha):
        console.print("[bold red]❌ Falha no login! Verifique e tente novamente.[/bold red]")
        return

    console.print("[bold green]✅ Login efetuado com sucesso![/bold green]")

    while True:
        console.print("""
[bold yellow]Escolha o serviço:[/bold yellow]
[1] 🏆 Rank King
[2] 📧 Trocar E-mail
[3] 🔐 Trocar Senha
[0] 🚪 Sair
""")

        opcao = console.input("[bold cyan]→ Escolha: [/bold cyan]")

        if opcao == "1":
            console.print("🏆 Aplicando Rank King...")
            try:
                cpm.set_player_rank()
                console.print("[bold green]✅ Rank King aplicado com sucesso![/bold green]")
            except Exception as e:
                console.print(f"[bold red]Erro: {e}[/bold red]")

        elif opcao == "2":
            novo_email = console.input("[bold cyan]📧 Novo e-mail: [/bold cyan]")
            try:
                cpm.change_email(novo_email)
                console.print("[bold green]✅ E-mail alterado com sucesso![/bold green]")
            except Exception as e:
                console.print(f"[bold red]Erro ao trocar e-mail: {e}[/bold red]")

        elif opcao == "3":
            nova_senha = console.input("[bold cyan]🔐 Nova senha: [/bold cyan]")
            try:
                cpm.change_password(nova_senha)
                console.print("[bold green]✅ Senha alterada com sucesso![/bold green]")
            except Exception as e:
                console.print(f"[bold red]Erro ao trocar senha: {e}[/bold red]")

        elif opcao == "0":
            console.print("[bold magenta]Saindo...[/bold magenta]")
            break
        else:
            console.print("[bold red]Opção inválida.[/bold red]")

        time.sleep(1.5)

if __name__ == "__main__":
    main()

