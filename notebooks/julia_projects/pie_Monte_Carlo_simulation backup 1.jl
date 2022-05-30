using GLMakie

fig = Figure(resolution=(3840, 2160))Figure()

ax1 = fig[1, 1] = Axis(fig,
    aspect=1, targetlimits=BBox(-1, 1, -1, 1),
    title="Dartboard",
    titlegap=48, titlesize=60, xautolimitmargin=(0, 0), xgridcolor=:black, xgridwidth=2,
    xticlabelsize=36, xticks=LineTicks(10), xticksize=18, yautolimitmargin=(0, 0), ygridcolor=:black, ygridwidth=2,
    yticlabelsize=36, yticks=LineTicks(10), yticksize=18
)