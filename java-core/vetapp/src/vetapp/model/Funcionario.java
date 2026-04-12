package vetapp.model;

public class Funcionario {

    private int idFuncionario;
    private String nome;
    private String funcao;
    private String telefone;
    private String email;

    public Funcionario() {
    }

    public Funcionario(String nome, String funcao, String telefone, String email) {
        this.nome = nome;
        this.funcao = funcao;
        this.telefone = telefone;
        this.email = email;
    }

    public int getIdFuncionario() {
        return idFuncionario;
    }

    public void setIdFuncionario(int idFuncionario) {
        this.idFuncionario = idFuncionario;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getFuncao() {
        return funcao;
    }

    public void setFuncao(String funcao) {
        this.funcao = funcao;
    }

    public String getTelefone() {
        return telefone;
    }

    public void setTelefone(String telefone) {
        this.telefone = telefone;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    @Override
public String toString() {
    return nome;
}
    
}