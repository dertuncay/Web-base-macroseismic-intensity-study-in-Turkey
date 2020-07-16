import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob, math

# Create Figure
fig, ax = plt.subplots(6,5, figsize=(20, 18))#, facecolor='w', edgecolor='k'
# Remove unused axes
ax[-1, -1].axis('off')
ax[-1, -2].axis('off')
ax[-1, -3].axis('off')
ax[-1, -4].axis('off')
# fig.subplots_adjust(hspace = .5, wspace=.001)
ax = ax.ravel()

csvs = sorted(glob.glob('*.csv'))
for ax_c, csv in enumerate(csvs):
	df = pd.read_csv(csv)
	eq_name = csv.split('_')[0]
	# fig, ax = plt.subplots(nrows=1)
	bins = [0, 9, 19, 29, 39, 49, 59, 69, 79, 89, 99, 1090]
	df['DISTANCE_BINS'] = pd.cut(x=df['DISTANCE'], bins=bins)
	print(eq_name)
	unique_bins = df.DISTANCE_BINS.unique()
	x_data = []; y_data = []; weights = []; weights_no100plus = []; x_data_no100plus = []; y_data_no100plus = [];
	for i, bin in enumerate(unique_bins.sort_values()):
		tmp = df.loc[df['DISTANCE_BINS'] == bin]
		w_av = np.average(tmp.AV_MMI, weights=tmp.NO_DP)
		max_mmi = tmp.MAX_MMI.max()
		min_mmi = tmp.MIN_MMI.min()
		# x = distance
		if bin.right == 1090:
			x = (bin.left + 109)/ 2.
		else:
			x = (bin.left + bin.right)/ 2.
		x_data.append(x)
		# Calculated MMI
		if tmp.CALC_MMI.max() > 10:
			calc_MMI = math.floor(tmp.CALC_MMI.max()/10)
		else:
			calc_MMI = tmp.CALC_MMI.max()
		# y = average MMI
		y = w_av - calc_MMI
		y_data.append(y)
		# upper_MMI = CALC_MMI - MAX_MMI
		upper_MMI = max_mmi - calc_MMI
		# lower_MMI = CALC_MMI - MIN_MMI
		lower_MMI = min_mmi - calc_MMI
		# asymmetric_error = [[lower_MMI], [upper_MMI]]
		# print(x,y,lower_MMI,upper_MMI)
		ax[ax_c].scatter(x,y,c='k',marker = 'o')
		ax[ax_c].vlines(x = x, ymin = lower_MMI, ymax = upper_MMI, color = 'k')
		# Put number of data points
		ax[ax_c].text(x=x-0.1,y = min(y,lower_MMI,upper_MMI)-0.7,s=str(np.sum(tmp.NO_DP)))
		# ax.errorbar(x, y, yerr=asymmetric_error, fmt='o', c = 'k', elinewidth = 3)
		ax[ax_c].set_title(eq_name)
		ax[ax_c].hlines(y=0,xmin = 0, xmax = 110,color='r',linestyles='--')
		ax[ax_c].set_xlim([0,110])
		ax[ax_c].set_ylim([-5,5])
		ax[ax_c].set_xticks(np.arange(0, 110, 10))
		ax[ax_c].set_yticks(np.arange(-5, 5, 1))
		ax[ax_c].set_xticklabels(['0', '10', '20', '30', '40', '50','60', '70', '80', '90', '100+'])
		ax[ax_c].set_xlabel('Distance (km)')
		ax[ax_c].set_ylabel('Residual')
		ax[ax_c].grid(True)
		# Weights
		weights.append(np.sum(tmp.NO_DP))
		# Weights without +100km
		if bin.right != 1090:
			weights_no100plus.append(np.sum(tmp.NO_DP))
			x_data_no100plus.append(x)
			y_data_no100plus.append(y)
	# Line fitting
	if len(y_data) > 1:
		z = np.polyfit(x_data, y_data, 1)
		p = np.poly1d(z)
		xp = np.linspace(0, 110, 500)
		ax[ax_c].plot(xp,p(xp),c='k',ls = ':', lw = 1.5)
	# 	# Weighted Least Square (all bins)
	# 	W = np.asarray(weights)
	# 	W = np.true_divide(W, np.sum(W))
	# 	z = np.polyfit(x_data, y_data, 1,w = W)
	# 	p = np.poly1d(z)
	# 	xp = np.linspace(0, 110, 500)
	# 	ax[ax_c].plot(xp,p(xp),c='b',ls = 'dashdot', lw = 1.5)
	# if len(y_data_no100plus) > 1:
	# 	# Weighted Least Square (without +100km)
	# 	W = np.asarray(weights_no100plus)
	# 	W = np.true_divide(W, np.sum(W))
	# 	z = np.polyfit(x_data_no100plus, y_data_no100plus, 1,w = W)
	# 	p = np.poly1d(z)
	# 	xp = np.linspace(0, 110, 500)
	# 	ax[ax_c].plot(xp,p(xp),c='g',ls = '--', lw = 1.5)

	# plt.show()
# plt.savefig('Figures/' + eq_name + '.png',dpi=300)
fig.tight_layout()
plt.savefig('Figures/results.png')
plt.close('all')
