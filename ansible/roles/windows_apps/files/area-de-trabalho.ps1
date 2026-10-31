# Gerado pelo Ansible (role windows_apps). Roda a cada entrada no Windows, na conta de
# quem entra (HKLM\...\Run): área de trabalho só com "Este Computador" e o Firefox.
# Só apaga atalhos (.lnk e .url); arquivos e pastas da pessoa ficam onde estão.

# Ícones do sistema: 0 = mostra, 1 = esconde.
$icones = 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\HideDesktopIcons\NewStartPanel'
New-Item -Path $icones -Force | Out-Null
@{
  '{20D04FE0-3AEA-1069-A2D8-08002B30309D}' = 0   # Este Computador
  '{645FF040-5081-101B-9F08-00AA002F954E}' = 1   # Lixeira
  '{59031a47-3f72-44a7-89c5-5595fe6b30ee}' = 1   # Pasta do usuário
  '{F02C1A0D-BE21-4350-88B0-7367FC96EF3C}' = 1   # Rede
  '{5399E694-6CE5-4D6C-8FCE-1D8870FDCBA0}' = 1   # Painel de Controle
}.GetEnumerator() | ForEach-Object {
  Set-ItemProperty -Path $icones -Name $_.Key -Value $_.Value -Type DWord
}

# Atalhos de programas na área de trabalho da pessoa, menos o do Firefox.
$area = [Environment]::GetFolderPath('Desktop')
Get-ChildItem -Path $area -File -Force -ErrorAction SilentlyContinue |
  Where-Object { $_.Extension -in '.lnk', '.url' -and $_.BaseName -notlike 'Firefox*' } |
  Remove-Item -Force -ErrorAction SilentlyContinue

# Atualiza a área de trabalho sem precisar sair e entrar.
Add-Type -Namespace TI -Name Shell -MemberDefinition '[DllImport("shell32.dll")] public static extern void SHChangeNotify(int e, int f, IntPtr a, IntPtr b);'
[TI.Shell]::SHChangeNotify(0x8000000, 0, [IntPtr]::Zero, [IntPtr]::Zero)
