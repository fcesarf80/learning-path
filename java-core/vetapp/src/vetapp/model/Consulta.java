package vetapp.model;

public class Consulta {

    private int idConsulta;
    private String dataConsulta;
    private String horaConsulta;
    private String observacao;
    private int idAnimal;
    private int idFuncionario;

    public Consulta() {
    }

    public Consulta(String dataConsulta, String horaConsulta, String observacao, int idAnimal, int idFuncionario) {
        this.dataConsulta = dataConsulta;
        this.horaConsulta = horaConsulta;
        this.observacao = observacao;
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

    public String getHoraConsulta() {
        return horaConsulta;
    }

    public void setHoraConsulta(String horaConsulta) {
        this.horaConsulta = horaConsulta;
    }

    public String getObservacao() {
        return observacao;
    }

    public void setObservacao(String observacao) {
        this.observacao = observacao;
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