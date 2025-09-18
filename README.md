# q-developer-quest-tdc-2025
projeto amazon Q developer
# AWS CLI v2

This bundle contains a built executable of the AWS CLI v2.

## Installation

To install the AWS CLI v2, run the `install` script:
```
$ sudo ./install 
You can now run: /usr/local/bin/aws --version
```
This will install the AWS CLI v2 at `/usr/local/bin/aws`.  Assuming
`/usr/local/bin` is on your `PATH`, you can now run:
```
$ aws --version
```


### Installing without sudo

If you don't have ``sudo`` permissions or want to install the AWS
CLI v2 only for the current user, run the `install` script with the `-b`
and `-i` options:
```
$ ./install -i ~/.local/aws-cli -b ~/.local/bin
``` 
This will install the AWS CLI v2 in `~/.local/aws-cli` and create
symlinks for `aws` and `aws_completer` in `~/.local/bin`. For more
information about these options, run the `install` script with `-h`:
```
$ ./install -h
```

### Updating

If you run the `install` script and there is a previously installed version
of the AWS CLI v2, the script will error out. To update to the version included
in this bundle, run the `install` script with `--update`:
```
$ sudo ./install --update
```


### Removing the installation

To remove the AWS CLI v2, delete the its installation and symlinks:
```
$ sudo rm -rf /usr/local/aws-cli
$ sudo rm /usr/local/bin/aws
$ sudo rm /usr/local/bin/aws_completer
```
Note if you installed the AWS CLI v2 using the `-b` or `-i` options, you will
need to remove the installation and the symlinks in the directories you
specified.

## Estimativa de Custos AWS

### Serviços Comuns e Preços (região us-east-1)

#### Amazon EC2
- **t3.micro**: $0.0104/hora (~$7.59/mês)
- **t3.small**: $0.0208/hora (~$15.18/mês)
- **t3.medium**: $0.0416/hora (~$30.37/mês)

#### Amazon S3
- **Standard Storage**: $0.023/GB/mês
- **Requests GET**: $0.0004 por 1.000 requests
- **Requests PUT**: $0.005 por 1.000 requests

#### AWS Lambda
- **Requests**: $0.20 por 1M requests
- **Duration**: $0.0000166667 por GB-segundo
- **Free Tier**: 1M requests/mês + 400.000 GB-segundos/mês

#### Amazon RDS (MySQL)
- **db.t3.micro**: $0.017/hora (~$12.41/mês)
- **Storage (gp2)**: $0.115/GB/mês

### Exemplo de Arquitetura Básica (Custo Mensal)
```
Aplicação Web Simples:
- EC2 t3.micro (1 instância): $7.59
- S3 (100GB storage): $2.30
- RDS db.t3.micro: $12.41
- Lambda (dentro do free tier): $0.00

Total Estimado: ~$22.30/mês
```

### Ferramentas de Estimativa
- **AWS Pricing Calculator**: https://calculator.aws
- **AWS Cost Explorer**: Para análise de custos históricos
- **AWS Budgets**: Para alertas de gastos

*Preços sujeitos a alteração. Consulte sempre o AWS Pricing Calculator para estimativas atualizadas.*
