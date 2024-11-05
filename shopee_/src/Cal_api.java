
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class Cal_api {
    private static String url_api01 = "https://affiliate.shopee.co.th/api/v3/offer/product/list?list_type=0&sort_type=1&page_offset=0&page_limit=20&client_type=1";
    private static String url_api02 = "https://affiliate.shopee.co.th/offer/product_offer";
    private static String login_01 = "https://dem.shopee.com/dem/janus/v1/app-auth/login";

    public static void main(String[] args) {

        Get object_api = new Get();
        object_api.getApi01(url_api01);
    }

}

class Get {
    Get() {

    }

    public void getApi01(String url) {
        try {
            HttpClient client = HttpClient.newHttpClient();
            HttpRequest request = HttpRequest.newBuilder()
                    .uri(new URI(
                            url))
                    .header("Accept", "application/json")
                    .GET()
                    .build();

            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
            System.out.println("Response: " + response.body());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
