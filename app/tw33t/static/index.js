Vue.component('get-tweets', {
  data: function () {
    return {
      screen_name: '',
      latest_tweets: [],
      tweet: {},
      input_valid: true,
      no_output: false,
      loading: false
    }
  },

  methods: {
    fetchTweets: function () {

      // If input is filled, then get request to the server
      if (!/\S/.test(this.screen_name) == '') {
        this.input_valid = true;
        const url = '/tweets/' + this.screen_name + '/';
        this.loading = true;
        axios.get(url)
          .then(response => {
            this.latest_tweets = response.data;
            this.loading = false;
          })

        // Check if user do not have any tweet response from server
        if (this.latest_tweets.length == 0) {
          this.no_output = true;
        }
      }

      // If no, prompt the message error back to user
      else {
        this.input_valid = false;
      }
    }
  },

  template: `
    <div class="center user-input-wrapper">
      <input v-model="screen_name" class="user-input" placeholder="Add your screen name">

      <div class="submit-button-wrapper">
        <button :disabled="isLoading" v-on:click="fetchTweets" class="submit-button">
          {{ isLoading ? '...' : 'tweets' }}
        </button>
      </div>
      <div v-if="!input_valid" class="aler-error">Oop!!! You did not type anything above.</div>
      <div v-else-if="latest_tweets.length > 0">
        <div class="tweet-list-wrapper">
          <div v-for="tweet in latest_tweets">
            <div class="tweet-li-date"> {{ tweet.creation_date }} </div>
            <div class="tweet-list-detail">{{ tweet.content }}</div>
          </div>
        </div>
      </div>
      <div v-else-if="no_output" class="aler-error">Oop!!! This user do not have any tweets.</div>
    </div>
    `
})

new Vue({ el: '#vue-tweets-app' })
