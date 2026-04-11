package vetapp.model;

public class Cliente {

    private int idCliente;
    private String nome;
    private String telefone;
    private String email;
    private String endereco;

    // O construtor vazio deve ficar AQUI DENTRO
    public Cliente() {
    }
    
    // Construtor completo
    public Cliente(String nome, String telefone, String email, String endereco) {
    this.nome = nome;
    this.telefone = telefone;
    this.email = email;
    this.endereco = endereco; // Adicione esta linha
}


    public Cliente(String nome, String telefone, String email) {
        this.nome = nome;
        this.telefone = telefone;
        this.email = email;
    }

    public int getIdCliente() {
        return idCliente;
    }

    public void setIdCliente(int idCliente) {
        this.idCliente = idCliente;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
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
    
    public String getEndereco() {
    return endereco;
    }

    public void setEndereco(String endereco) {
    this.endereco = endereco;
    }
}
