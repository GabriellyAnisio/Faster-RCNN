from PIL import Image
import os

# Caminho da pasta com as imagens PNG
input_folder = "VOC2007-test/JPEGImages"
output_folder = "VOC2007-test/JPEGImages2"  # Pasta onde salvar as imagens convertidas

# Cria a pasta de saída se não existir
os.makedirs(output_folder, exist_ok=True)

# Loop por todas as imagens na pasta
for file in os.listdir(input_folder):
    if file.endswith(".png"):  # Verifica se é PNG
        img_path = os.path.join(input_folder, file)
        img = Image.open(img_path).convert("RGB")  # Converte para RGB

        # Novo nome trocando a extensão para .jpg
        new_file = file.replace(".png", ".jpg")
        img.save(os.path.join(output_folder, new_file), "JPEG", quality=95)

print("Conversão concluída!")
