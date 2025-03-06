def inference(self, G_path, n_generate=1000, n_output=30, show=False):
	"""
	1. G_path is the path for Generator ckpt
	2. You can use this function to generate final answer
	"""
	self.G.load_state_dict(torch.load(G_path))
	self.G.cuda()
	self.G.eval()
	z = Variable(torch.randn(n_generate, self.config["z_dim"])).cuda()
	imgs = (self.G(z).data + 1) / 2.0
	
	os.makedirs('output', exist_ok=True)
	for i in range(n_generate):
		torchvision.utils.save_image(imgs[i], f'output/{i+1}.jpg')
	
	if show:
		row, col = n_output//10 + 1, 10
		grid_img = torchvision.utils.make_grid(imgs[:n_output].cpu(), nrow=row)
		plt.figure(figsize=(row, col))
		plt.imshow(grid_img.permute(1, 2, 0))
		plt.show()

workspace_dir = '.'

# save the 1000 images into ./output folder
inference(f'{workspace_dir}/checkpoints/2022-03-31_15-59-17_GAN/G_0.pth') # you have to modify the path when running this line