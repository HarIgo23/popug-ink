# Final

- [x]  Разобрать каждое требование на составляющие (актор, команда, событие, query). Определить, как все бизнес цепочки будут выглядеть и на какие шаги они будут разбиваться.
    
    ### **Таск-трекер**
    
    1. Авторизация в таск-трекере
        - Actor — Account
        - Command — Auth
        - Data — ???
        - Event — Account.Authorised
    2. Новые таски может создавать кто угодно (администратор, начальник, разработчик, менеджер и любая другая роль). У задачи должны быть описание, статус (выполнена или нет) и попуг, на которого заассайнена задача.
        - Actor — Any user(account with any role)
        - Command — Create task
        - Data — Task + Account public id
        - Event — Task.Assigned
    3. Менеджеры или администраторы должны иметь кнопку «заассайнить задачи».
        - Actor — Manager or Admin user(account with “manager” or “admin” role)
        - Command — Assign task
        - Data — Task + Account public id
        - Event — Task.Assigned
    4. Каждый сотрудник должен иметь возможность отметить задачу выполненной
        - Actor — Account
        - Command — Resolve Task
        - Data — Task
        - Event — Task.Resolved
    
    ### **Аккаунтинг: кто сколько денег заработал**
    
    1. Авторизация в дешборде аккаунтинга должна выполняться через общий сервис аутентификации UberPopug Inc.
        - Actor — Account
        - Command — Auth
        - Data — ???
        - Event — Account.Authorised
    2. У счёта должен быть аудитлог того, за что были списаны или начислены деньги, с подробным описанием каждой из задач.
        - Actor — “Balance.Changed” event
        - Command — Create audit record
        - Data — Balance + Task  + Account public id
        - Event — ???
    3. Деньги списываются сразу после ассайна на сотрудника, 
        - Actor — “Task.Assigned” event
        - Command — Charge money
        - Data — Balance + Account public id
        - Event — Balance.Changed
    4. Начисляются деньги после выполнения задачи.
        - Actor — “Task.Resolved” event
        - Command — Pay money
        - Data —  Balance + Account public id
        - Event — Balance.Changed
    5. В конце дня необходимо считать сколько денег сотрудник получил за рабочий день
        - Actor — “End of day” event
        - Command — Calculate pay off
        - Data — Balance
        - Event — Balance.PayOffCalculated
    6. Отправлять на почту сумму выплаты.
        - Actor — “Balance.PayOffCalculated” event
        - Command — Notificate user about pay off
        - Data — Account
        - Event — ??
    7. После выплаты баланса (в конце дня) он должен обнуляться.
        - Actor — “Balance.PayOffCalculated” event
        - Command — Clear balance
        - Data — Account
        - Event — ??
    8. После выплаты баланса в аудитлоге всех операций аккаунтинга должно быть отображено, что была выплачена сумма.
        - Actor — “Balance.PayOffCalculated” event
        - Command —  Create audit record
        - Data — Balance
        - Event — ??
- [x]  Построить модель данных для системы и модель доменов. Рисовать можно в любом удобном инструменте (включая обычную бумагу), главное, чтобы это было не только у вас в голове, но и где-то вовне. Благодаря этому вы сможете сфокусироваться на отдельной части системы, не думая о других. А также показать свое решение одногрупникам/коллегам.
    
    ### **Data model**
    
    ![Popug ink - Data models.jpg](images/Popug_ink_-_Data_models.jpg)
    
    ### **Domen model**
    
    ![Popug ink - Domain models.jpg](images/Popug_ink_-_Domain_models.jpg)
    
- [x]  Определить, какие общие данные нужны для разных доменов и как связаны данные между разными доменами.
    - Balance - Account and Task
    - Auth - No need additional data
    - Task - Account
- [x]  Разобраться, какие сервисы, кроме тудушника, будут в нашей системе и какие между ними могут быть связи (как синхронные, так и асинхронные).
    1. Auth service
    2. Balance service
    3. Task service
    
    - Апдейты аккаунта - Balance и Task - async
    - Апдейты таски - Balance - async
    - Вызов изменений аккаунта - async
    - Создание сущностей- sync
    - Авторизация - sync
    
- [x]  Определить все бизнес события, необходимые для работы системы. Отобразить кто из сервисов является продьюсером, а кто консьюмером бизнес событий.
    - Account.Authorised — None
    - Task.Assigned — pr: Task, c: Balance
    - Task.Resolved — pr: Task, c: Balance
    - Balance.Changed — pr: Balance, c: Balance
    - End of day — pr: None, c: Balance
- [x]  Выписать все CUD события и какие данные нужны для этих событий, которые необходимы для работы системы. Отобразить кто из сервисов является продьюсером, а кто консьюмером CUD событий.
    - Account CUD — pr: Account, c: Balance, Task
    - Task CUD — pr: Task, c: Balance