#!/bin/bash

echo "Iniciando projeto calculadora"
BACKUP_NAME="usuarios_backup_calc_$(date +%d-%m-%y)"
mkdir -p projetotestelinux/backup_calc
echo "Diga seu nome calculador: "
read NOME_CALC

ARQUIVO_LOGIN="projetotestelinux/backup_calc/log${NOME_CALC}_$(date +%H-%M-%S).txt"
echo "Iniciando script da calculadora $(date +%d-%m-%y_%H:%M:%S)" > "$ARQUIVO_LOGIN"
echo "-------------------------------------------------------" >> "$ARQUIVO_LOGIN"


python3 calculadora.py "$NOME_CALC" >> "$ARQUIVO_LOGIN"

echo "---------------------------------------------" >> "$ARQUIVO_LOGIN"
echo "Backup realizado com sucesso: $ARQUIVO_LOGIN"
