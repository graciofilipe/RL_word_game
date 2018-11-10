import numpy as np


def run_actor_critic_traces(agent,
                            environment,
                            start_state,
                            n_iter,
                            alpha_th,
                            alpha_w,
                            lambda_th,
                            lambda_w,
                            gama):

    n_w = len(agent.return_w())
    n_th = len(agent.return_th())


    for _ in range(n_iter):
        state = start_state
        environment.set_state(state)
        z_w = np.array([0 for _ in range(n_w)])
        z_th = np.array([0 for _ in range(n_th)])
        I = 1
        terminal_flag = False
        while terminal_flag == False:

            action = agent.return_action(state, environment)
            new_state, reward, terminal_flag = environment.return_state_and_reward_post_action(action)
            environment.set_state(new_state)

            new_state_value = agent.state_value_estimate(new_state)
            state_value = agent.state_value_estimate(state)
            if terminal_flag:
                new_state_value = 0
            delta = reward + gama*new_state_value - state_value

            value_estimate_gradient = agent.state_value_estimate_gradient(state=state)
            z_w = gama*lambda_w*z_w + value_estimate_gradient


            ln_policy_gradient = agent.ln_policy_gradient(state=state, action=action, environment=environment)
            z_th = gama*lambda_th*z_th + I*ln_policy_gradient

            w_inc = alpha_w*delta*z_w
            agent.increment_w(w_increment=w_inc)

            th_inc = alpha_th * delta * z_th
            agent.increment_th(th_increment=th_inc)

            I = gama*I
            state = new_state

    return agent




