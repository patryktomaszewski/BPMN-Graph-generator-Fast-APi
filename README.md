# BPMN Graph generator Fast APi

Run instruction:
- 
From root directory run
- `docker-compose build`
- `docker-compose up`

One endpoint is accessible:
`0.0.0.0:8088/generate_graph/`

To generate graph make post request on above endpoint, in request body pass csv file at key: `file`

Example:
![img.png](img.png)

Example csv file is placed in `sample_data` directory

In response you get stringified .dot file.
You can generate graph in gif format by using e.g: https://www.npmjs.com/