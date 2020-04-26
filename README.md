# QuantumRobot_Circuit
Quantum Robots or Quantum Systems

#!/usr/bin/env python3
#
# Copyright 2019 the original author or authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# vector-and-ibmq.py
# Demonstration of an Anki Vector robot leveraging an IBM quantum computer
# Note: For ideas on expanding the number of responses from 2 to 8 or more, see the original
#       quantum 8-ball Jupyter notebook that Oleksii Lialka created as a Qiskit tutorial.
# https://github.com/Qiskit/qiskit-tutorials/blob/master/community/hello_world/quantum_8ball.ipynb



#Import Qiskit After Installing
import qiskit
from qiskit import IBMQ
from qiskit import*
#Build a Quantum Circuit
qr= QuantumRegister(1)
cr=ClassicalRegister(1)
qc=QuantumCircuit(qr,cr)
#Plot this cicruit using matplotlib 
qc.draw()
      
q0_0: 
      
c0_0: 
      
%matplotlib inline
qc.draw('mpl')

qc.measure(qr,c)
<qiskit.circuit.instructionset.InstructionSet at 0x17b8e864648>
qc.draw(output='mpl')

job = execute(qc, backend=Aer.get_backend('qasm_simulator'), shots=1)
result = job.result().get_counts(qc)
qc.draw('mpl'%result)

answer(result)
#Activate Aer Quantum Simulator
simulator =Aer.get_backend('qasm_simulator')
result = execute(qc, backend = simulator).result()
from qiskit.tools.visualization import plot_histogram
plot_histogram(result.get_counts(qc))

#Load IBM Account and Run 

IBMQ.load_account()
<AccountProvider for IBMQ(hub='ibm-q', group='open', project='main')>
provider = IBMQ.get_provider('ibm-q')
qcomp = provider.get_backend('ibmq_16_melbourne')
job=execute(qc,backend=qcomp)
from qiskit.tools.monitor import job_monitor
job_monitor(job)
Job Status: job has successfully run
result=job.result()
plot_histogram(result.get_counts(qc))

 
