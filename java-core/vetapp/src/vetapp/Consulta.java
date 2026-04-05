package vetapp;

public class Consulta {

    private int idConsulta;
    private String dataConsulta;
    private String descricao;
    private double valor;
    private int idAnimal;
    private int idFuncionario;

    public Consulta() {
    }

    public Consulta(String dataConsulta, String descricao, double valor, int idAnimal, int idFuncionario) {
        this.dataConsulta = dataConsulta;
        this.descricao = descricao;
        this.valor = valor;
        this.idAnimal = idAnimal;
        this.idFuncionario = idFuncionario;
    }

    public int getIdConsulta() {
        return idConsulta;
    }

    public void setIdConsulta(int idConsulta) {
        this.idConsulta = idConsulta;
    }

    public String getDataConsulta() {
        return dataConsulta;
    }

    public void setDataConsulta(String dataConsulta) {
        this.dataConsulta = dataConsulta;
    }

    public String getDescricao() {
        return descricao;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }

    public double getValor() {
        return valor;
    }

    public void setValor(double valor) {
        this.valor = valor;
    }

    public int getIdAnimal() {
        return idAnimal;
    }

    public void setIdAnimal(int idAnimal) {
        this.idAnimal = idAnimal;
    }

    public int getIdFuncionario() {
        return idFuncionario;
    }

    public void setIdFuncionario(int idFuncionario) {
        this.idFuncionario = idFuncionario;
    }
}