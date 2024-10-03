primero hicimemos el urdf, despues hicimos el robot/xacro y robot.gazebo.
Xacro permite crear archivos XML más organizados y cortos. Por ejemplo, puede hacer que estos archivos sean más organizados ya que está utilizando XML para describir robots en archivos URDF.

Archivos incluidos
Por ejemplo, tiene una gran sección para describir la integración de Gazebo con el robot. Puede ponerlo en un archivo separado. Compruebe cómo.

Cree un nuevo archivo robot.gazebo
Cambie el nombre del archivo original robot.urdf por robot.xacro
Corte todas las etiquetas <gazebo> de robot.xacro y péguelas en el nuevo archivo robot.gazebo, dentro de la siguiente plantilla:
Corte todas las etiquetas <gazebo> de robot.xacro y péguelas en el nuevo archivo robot.gazebo, dentro de la siguiente plantilla:

 Copiar y pegar


<?xml version="1.0"?>
<robot>
    <!-- Paste here -->
</robot>
Por último, incluya este nuevo archivo en el archivo de descripción del robot. También deberá añadir esta nueva definición Xacro en la etiqueta del robot:

 Copiar y pegar


<?xml version="1.0" ?>

<robot name="robot" xmlns:xacro="http://www.ros.org/wiki/xacro">

    <xacro:include filename="$(find robot_description)/urdf/robot.gazebo" />
    
    <!-- Link - chassis -->
    ...
    
</robot>
Para que este archivo XACRO sea comprensible para Gazebo, conviértalo justo antes de desovar el modelo. Abra el archivo spawn.launch y sustituya el parámetro robot_descript por el siguiente:


    <param name="robot_description" command="$(find xacro)/xacro --inorder '$(find robot_description)/urdf/robot.xacro'"/>
Esto convierte de XACRO a URDF, por lo que la descripción vuelve a su estado original, como URDF, ¡y el desarrollador puede utilizar lo mejor de XACRO