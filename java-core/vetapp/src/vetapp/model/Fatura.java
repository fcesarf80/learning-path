package vetapp.model;

public class Fatura {

    private int idFatura;
    private String dataEmissao;
    private double valorTotal;
    private String estado;
    private int idCliente;
    private int idConsulta;

    public Fatura() {
    }

    public Fatura(String dataEmissao, double valorTotal, String estado, int idCliente, int idConsulta) {
        this.dataEmissao = dataEmissao;
        this.valorTotal = valorTotal;
        this.estado = estado;
        this.idCliente = idCliente;
        this.idConsulta = idConsulta;
    }

    public int getIdFatura() {
        return idFatura;
    }

    public void setIdFatura(int idFatura) {
        this.idFatura = idFatura;
    }

    public String getDataEmissao() {
        return dataEmissao;
    }

    public void setDataEmissao(String dataEmissao) {
        this.dataEmissao = dataEmissao;
    }

    public double getValorTotal() {
        return valorTotal;
    }

    public void setValorTotal(double valorTotal) {
        this.valorTotal = valorTotal;
    }

    public String getEstado() {
        return estado;
    }

    public void setEstado(String estado) {
        this.estado = estado;
    }

    public int getIdCliente() {
        return idCliente;
    }

    public void setIdCliente(int idCliente) {
        this.idCliente = idCliente;
    }

    public int getIdConsulta() {
        return idConsulta;
    }

    public void setIdConsulta(int idConsulta) {
        this.idConsulta = idConsulta;
    }
}