from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from Particulas import Particulas
from particula import Particula

# la clase mainwindow hereda lo de QMainWindow
class MainWindow(QMainWindow): 
    def __init__(self):
        super(MainWindow, self).__init__()

        self.particula = Particula()
        self.particulas = Particulas()
        #al declarar el objeto de manera globar ya podemos crear particulas

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Inicio_pushButton.clicked.connect(self.agregar_Particula_Inicio)
        self.ui.Final_pushButton.clicked.connect(self.agregar_Particula_Final)
        self.ui.pushButton_2.clicked.connect(self.mostrar_Particula)
        
        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)

        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_titulo)


    @Slot()
    def buscar_titulo(self):
        id = self.ui.buscar_lineEdit.text()
        encontrado = False
        for particula in self.particulas:
            if id == particula.id:
                self.ui.tabla.clear() #vacia la filas para poner el libro
                self.ui.tabla.setRowCount(1) #nada mas tendra una fila
                id_widget = QTableWidgetItem(particula.id)
                origenX_widget = QTableWidgetItem(str(particula.origenX))
                origenY_widget = QTableWidgetItem(str(particula.origenY))
                destinoX_widget = QTableWidgetItem(str(particula.destinoX))
                destinoY_widget = QTableWidgetItem(str(particula.destinoY))
                velocidad_widget = QTableWidgetItem(str(particula.velocidad))
                colorR_widget = QTableWidgetItem(str(particula.colorR))
                colorG_widget = QTableWidgetItem(str(particula.colorG))
                colorB_widget = QTableWidgetItem(str(particula.colorB))
                distancia_widget = QTableWidgetItem(str(particula.distancia))

                self.ui.tabla.setItem(0, 0,id_widget)
                self.ui.tabla.setItem(0, 1,origenX_widget)
                self.ui.tabla.setItem(0, 2,origenY_widget)
                self.ui.tabla.setItem(0, 3,destinoX_widget)
                self.ui.tabla.setItem(0, 4,destinoY_widget)
                self.ui.tabla.setItem(0, 5,velocidad_widget)
                self.ui.tabla.setItem(0, 6,colorR_widget)
                self.ui.tabla.setItem(0, 7,colorG_widget)
                self.ui.tabla.setItem(0, 8,colorB_widget)
                self.ui.tabla.setItem(0, 9,distancia_widget)
                encontrado = True
                return 
        if not encontrado:
            QMessageBox.warning(
                self,
                "Atencion",
                f'ERROR -> La Particula con el ID: "{id}" no se encontro'
            )
            



    @Slot()
    def mostrar_tabla(self):
        self.ui.tabla.setColumnCount(10)
        headers = ["ID","Origen X","Origen Y","Destino X", "Destino Y","Velocidad","Color R","Color G","Color B","Distancia"]
        self.ui.tabla.setHorizontalHeaderLabels(headers) # en la cabecera imprime los nombres

        self.ui.tabla.setRowCount(len(self.particulas)) # crea la cantidad de lineas dependiendo de las particulas que hemmos insertado

        row = 0
        for particula in self.particulas:
            id_widget = QTableWidgetItem(particula.id)
            origenX_widget = QTableWidgetItem(str(particula.origenX))
            origenY_widget = QTableWidgetItem(str(particula.origenY))
            destinoX_widget = QTableWidgetItem(str(particula.destinoX))
            destinoY_widget = QTableWidgetItem(str(particula.destinoY))
            velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            colorR_widget = QTableWidgetItem(str(particula.colorR))
            colorG_widget = QTableWidgetItem(str(particula.colorG))
            colorB_widget = QTableWidgetItem(str(particula.colorB))
            distancia_widget = QTableWidgetItem(str(particula.distancia))

            self.ui.tabla.setItem(row, 0,id_widget)
            self.ui.tabla.setItem(row, 1,origenX_widget)
            self.ui.tabla.setItem(row, 2,origenY_widget)
            self.ui.tabla.setItem(row, 3,destinoX_widget)
            self.ui.tabla.setItem(row, 4,destinoY_widget)
            self.ui.tabla.setItem(row, 5,velocidad_widget)
            self.ui.tabla.setItem(row, 6,colorR_widget)
            self.ui.tabla.setItem(row, 7,colorG_widget)
            self.ui.tabla.setItem(row, 8,colorB_widget)
            self.ui.tabla.setItem(row, 9,distancia_widget)

            row += 1 # incrementamos el contador de fila para que no se escriban encima
        
    @Slot()
    def action_abrir_archivo(self):
        #print('Abrir_archivo')
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo', #el nombre del archivo
            '.', #donde lo va a guardar, en este caso en la carpeta del proyecto
            'JSON (*.json)' #Tipo de formato
        )[0]
        if self.particulas.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Éxito",
                "Se abrió el archivo " + ubicacion
            )
        else:
            QMessageBox.information(
                self,
                "Error",
                "Error al abrir el archivo " + ubicacion
            )
        
    @Slot()
    def action_guardar_archivo(self):
        #print('Guardar_archivo')
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo', #el nombre del archivo
            '.', #donde lo va a guardar, en este caso en la carpeta del proyecto
            'JSON (*.json)' #Tipo de formato
        )[0]
        print(ubicacion)
        if self.particulas.guardar(ubicacion):
            QMessageBox.information(
                self, #desde donde se manda
                "Éxito", #nombre de la ventana
                "Se pudo crear el archivo " + ubicacion #mensaje
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo crear el archivo " + ubicacion
            )
            

    @Slot()
    def agregar_Particula_Inicio(self):
        id = self.ui.ID_lineEdit.text()
        origenX = self.ui.origenX_spinBox.value()
        origenY = self.ui.origenY_spinBox.value()
        destinoX = self.ui.destinoX_spinBox.value()
        destinoY = self.ui.destinoY_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        colorR = self.ui.R_spinBox.value()
        colorG = self.ui.G_spinBox.value()
        colorB = self.ui.B_spinBox.value()

        particula = Particula(id, origenX, origenY, destinoX, destinoY, velocidad, colorR, colorG, colorB)
        self.particulas.agregar_inicio(particula)
            

    @Slot()
    def agregar_Particula_Final(self):
        id = self.ui.ID_lineEdit.text()
        origenX = self.ui.origenX_spinBox.value()
        origenY = self.ui.origenY_spinBox.value()
        destinoX = self.ui.destinoX_spinBox.value()
        destinoY = self.ui.destinoY_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        colorR = self.ui.R_spinBox.value()
        colorG = self.ui.G_spinBox.value()
        colorB = self.ui.B_spinBox.value()

        particula = Particula(id, origenX, origenY, destinoX, destinoY, velocidad, colorR, colorG, colorB)
        self.particulas.agregar_final(particula)


    @Slot()
    def mostrar_Particula(self):
        #self.particulas.mostrar()
        self.ui.salida.clear(
            
        )
        self.ui.salida.insertPlainText(str(self.particulas))