import zipfile
import os
import pika
conection_parameters =  pika.ConnectionParameters(host='localhost')

conection = pika.BlockingConnection(conection_parameters)


channel = conection.channel()

channel.queue_declare(queue='start_image_processing')


def get_all_files_from_zip(zip_file):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        #os.mkdir(f'temp/{name}')

        for file in zip_ref.namelist():
            p = '/home/manuel/Documents/Pesonal/flask-aws-ocr/FILE-HANDLER/src/temp/'
            if file.endswith('.pdf'):
                zip_ref.extract(file, f'temp/')
                channel.basic_publish(exchange='', routing_key='start_image_processing', body=f'{p}{file}')
        conection.close()
