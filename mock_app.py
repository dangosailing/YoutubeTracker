from utils import ccv_mock, plot_ccv

def run_mock():
    data = ccv_mock.mock_sample()
    plot_ccv.generate_ccv_plot(data)

if __name__ == "__main__":
    run_mock()