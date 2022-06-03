using Flux, Images, MLDatasets, Plots
using Flux: crossentropy, onecold, onehotbatch, train!
using LinearAlgebra, Random, Statistics


Random.seed!(1)


#load mnist data set

x_train_raw, y_train_raw = MLDatasets.MNIST.traindata(Float32)
x_test_raw, y_test_raw = MLDatasets.MNIST.testdata(Float32)


# viewing training input(5)

x_train_raw

index = 1

img = x_train_raw[:, :, index]

colorview(Gray, img')


# viewing training lable or name of the taken image

y_train_raw
y_train_raw[index]

# viewing testing sample

x_test_raw
img = x_test_raw[:, :, index]

colorview(Gray, img')

# view testing lable
y_test_raw
y_test_raw[index]

# flatten input data, the 3d tensor to 2d metricx, reshaping the jl array

x_train = Flux.flatten(x_train_raw)
x_test = Flux.flatten(x_test_raw)


# onehot encoding for lables
y_train = onehotbatch(y_train_raw, 0:9)
y_test = onehotbatch(y_test_raw, 0:9)

# defining modle architecture for Multy layer Perceptron
# feeding training input and modle trys to learn the parameters

model = Chain(
    Dense(28 * 28, 32, relu),
    Dense(32, 10),
    softmax
)

# define loss function

loss(x, y) = crossentropy(model(x), y)

#track parameters

ps = params(model)

# select optimizer

learning_rate = 0.01
opt = ADAM(learning_rate)


# start training modle

loss_history = []
epochs = 500

for epoch in 1:epochs
    train!(loss, ps, [(x_train, y_train)], opt) #training

    #printing report
    train_loss = loss(x_train, y_train)
    push!(loss_history, train_loss)
    println("Epoch = $epoch : Training Loss = $train_loss")
end


#making predictions using the training data


# a 10 by 10thousand metrix sum of each column is 100% soo the probability is shown

y_hat_raw = model(x_test)

# one cold function converts metricx to column vectorsm using the index number which has high probability value
y_hat = onecold(y_hat_raw) .- 1 # subtract 1 from each index number to convert index number into lable

y = y_test_raw # compairing the predictions with trained data
mean(y_hat .== y)# it is 96% accurate

#displaying results

check = [y_hat[i] == y[i] for i in 1:length(y)]

index = collect(1:length(y))
# vscodedisplay(check_display) # 300 of 10000 data are missclassified or incorrect

# viewing mis-classified data 

misclass_index = 9
img = x_test_raw[:, :, misclass_index]

colorview(Gray, img')


# plotting a learning curve for the modle we trained
y[misclass_index]
y_hat[misclass_index]

gr(size = (600, 600))

p_l_curve = plot(1:epochs, loss_history,
    xlabel = "Epochs",
    ylabel = "Loss",
    title = "Learning Curve",
    legend = false,
    color = :blue,
    linewidth = 2
)
savefig(p_l_curve, "dlearning_curve.svg")