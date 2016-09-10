# Reinforcement Learning for Systematic Trading

This thesis has been realized for the obtention of the Master's in Mathematical 
Engineering at the Politecnico di Milano. The goal of this project was to apply
some reinforcement learning techniques to some classical financial problems, 
such as asset allocation and optimal order execution. 

## Repository Structure 

The repository is organized as follows:
* **Code**: contains the code for the project.
	* **Postprocessing** contains various Python scripts to process the output
	  data generated by the learning algorithms. 
	* **Preprocessing** contains various Python scripts to generate the input
	  data used by the learning algorithms. 
	* **Prototype** contains the Python prototype for this project. It is based
	  on the [PyBrain][http://pybrain.org/ "PyBrain"] library. 
	* **Thesis** contains the C++ implementation for this project.
* **Data**: contains the data used during the execution of the program. 
	* **Debug** contains some files produces by the learning algorithms for
	  debug purposes. 
	* **Input** contains the input files used by the learning algorithms.
	* **Output** contains the output files generated by the learning
	  algorithms.
	* **Parameters** contains the parameters of the learning algorithms. 
* **Launchers**: contains some scripts that can be used to launch the full
  execution pipeline for the project. 
* **Pacs**: contains the report for the "Advanced Programming and Scientific
  Computing" class at the Politecnico di Milano, for which this project was
  used.  
* **Report**: contains the main thesis document. 

## Authors

* **Pierpaolo Necchi** 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

