1/15/20, 4:06 PM

Render faster in blender 
1:
Scene->light paths bounces:1
Diffuse:1, glossy:1, transparency: 3-4, transmission 

2: 
Change the tile size:
Scene->performance: tiles x & y: 512x512
Gpu(128 to 1024)
Cpu(16x16)
3:
Reduce your samples: 
Scene->sampling: samples: render: 2500 or lower 
4: 
Denoising:

5: 
Turn of caustics 

Check MIS
