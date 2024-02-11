from abc import ABC, abstractmethod

class MineradorDeDados(ABC):
    def minerar(self):
        arquivo = self.abrir_arquivo()
        conteudo = self.ler_conteudo(arquivo)
        dados = self.extrair_dados(conteudo)
        pdf = self.analisar(dados)
        self.publicar_resultado(pdf)
    
    @abstractmethod
    def abrir_arquivo(self):
        pass

        
    @abstractmethod
    def ler_conteudo(self, arquivo):
        pass

        
    @abstractmethod
    def extrair_dados(self, conteudo):
        pass

    @abstractmethod
    def analisar(self, dados):
        pass

    @abstractmethod
    def publicar_resultado(self, pdf):
        pass

class MineradorExcel(MineradorDeDados):
    pass

class MineradorSiteIBGE(MineradorDeDados):
    pass

class MineradorCSV(MineradorDeDados):
    pass

class MineradorAPI_AlunosUEFS(MineradorDeDados):
    pass