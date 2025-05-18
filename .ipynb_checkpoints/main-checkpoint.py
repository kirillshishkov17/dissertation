def turbine_power(alpha, gamma, beta, u, D=154, rho=1.225):
    Cp = 4 * alpha * (1 - alpha)**2
    C_gamma = -0.0003*gamma**3 - 0.000025*gamma**2 + 0.997*gamma
    C_beta = -0.185 + 0.285*np.cos(0.105*beta)
    A = np.pi*(D/2)**2
    return 0.5 * Cp * C_gamma * C_beta * rho * A * u**3

# Параметры из статьи (раздел 2)
alpha = 0.33
gamma = 0  # градусы
beta = 0    # градусы
u = 8       # м/с
D = 154     # м

# Ожидаемая мощность для 5МВт турбины:
P_expected = 1.67  # МВт (из таблицы B.1 статьи)

